from ..models.db import db


def mock_dao_function_array():
    """Main DAO Function"""

    result_data = {
        'user': {
            'id': 0,
            'name': 'user_name',
            'email': 'user@name.com',
            'age': 0,
            'active': True,
            'updated_at': '2018-01-01'
        }
    }
    return result_data


# This is an example, remove this when building your project
def mock_dao_function_database():
    """
    Description Function

    :return: type
    :exception Exception: description Exception Type
    """

    try:
        sql = db.select([
            db.text("FIELD_01, FIELD_02")
        ]).select_from(
            db.text("TABLE_NAME WITH (NOLOCK)")
        )

        result = db.engine.execute(sql).fetchall()

        return result
    except Exception as e:
        raise e
