from sqlalchemy import func, extract, desc, select, case

from kivymd.app import MDApp

from models.area import Area
from models.ascent import Ascent
from models.grade import Grade


def get_ascents_per_area(
    min_grade_correspondence=1, max_grade_correpondence=19, area="All"
):
    """
    Get the number of ascents adn flashes per area
    :return: a list of tuple : (area, number of ascent, number of flash)
    """
    with MDApp.get_running_app().get_db_session() as session:
        query = (
            session.query(
                Area.name,
                func.count(Ascent.id),
                func.sum(case((Ascent.flash == True, 1), else_=0)),
            )
            .join(Ascent, Area.id == Ascent.area_id)
            .join(Grade, Grade.id == Ascent.grade_id)
            .filter(
                Grade.correspondence >= min_grade_correspondence,
                Grade.correspondence <= max_grade_correpondence,
            )
        )

        if area != "All":
            query = query.filter(Area.name == area)

        result = (
            query.group_by(Area.name)
            .order_by(func.count(Ascent.id).desc())
            .all()
        )
    return result


def get_average_grade(
    min_grade_correspondence=1, max_grade_correpondence=19, area="All"
):
    """
    Get the average climbed grade and the average flashed grade
    """
    with MDApp.get_running_app().get_db_session() as session:
        query = (
            session.query(
                func.avg(Grade.correspondence),
                func.avg(
                    case(
                        (Ascent.flash == True, Grade.correspondence),
                        else_=None,
                    )
                ),
            )
            .join(Ascent, Grade.id == Ascent.grade_id)
            .join(Area, Area.id == Ascent.area_id)
            .filter(
                Grade.correspondence >= min_grade_correspondence,
                Grade.correspondence <= max_grade_correpondence,
            )
        )

        if area != "All":
            query = query.filter(Area.name == area)

        average_grade, average_flash_grade = query.first()

        # If the average grade returned by the query is None (No ascent with
        # those filters), return None
        average_grade = get_avg_grade_from_corresp(average_grade, session)
        average_flash_grade = get_avg_grade_from_corresp(
            average_flash_grade, session
        )

    return average_grade, average_flash_grade


def get_avg_grade_from_corresp(average_correspondence, session):
    if not average_correspondence:
        return None
    average_grade = round(average_correspondence)
    average_grade = session.scalar(
        select(Grade.grade_value).where(Grade.correspondence == average_grade)
    )
    return average_grade
