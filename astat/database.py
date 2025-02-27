import os

from kivy.utils import platform

from models.grade import Grade


def get_db_path():
    db_filename = "astat.db"
    if platform == "win":
        data_dir = os.getcwd()
    elif platform == "android":
        # Get Android context
        from jnius import autoclass, cast

        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        context = cast("android.content.Context", PythonActivity.mActivity)

        # Get external storage path for your app
        file_p = cast("java.io.File", context.getExternalFilesDir(None))
        data_dir = file_p.getAbsolutePath()

    writable_db_path = os.path.join(data_dir, db_filename)

    return writable_db_path


def get_android_documents_path():
    """Returns the absolute path to the user's Documents directory on Android.
    """
    # Get Android context
    from jnius import autoclass, cast

    Environment = autoclass("android.os.Environment")
    documents_dir = Environment.getExternalStoragePublicDirectory(
        Environment.DIRECTORY_DOWNLOADS
    ).getAbsolutePath()
    return documents_dir
