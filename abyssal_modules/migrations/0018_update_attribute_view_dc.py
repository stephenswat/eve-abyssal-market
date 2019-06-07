from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abyssal_modules', '0017_attribute_stats'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE VIEW abyssal_modules_derived_attributes__view AS
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                "value",
                "attribute_id",
                "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                0.001 * "value" AS "value",
                10073 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10073 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 73
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                0.001 * "value" AS "value",
                11795 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 11795 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 1795
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * "value" AS "value",
                10147 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10147 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 147
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * ("value" - 1) AS "value",
                10213 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10213 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 213
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * (1 - "value") AS "value",
                10204 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10204 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 204
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * (1 - "value") AS "value",
                10974 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10974 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 974
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * (1 - "value") AS "value",
                10975 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10975 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 975
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * (1 - "value") AS "value",
                10976 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10976 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 976
            UNION
            SELECT
                0 AS "id",
                "module_id",
                "static_module_id",
                100 * (1 - "value") AS "value",
                10977 AS "attribute_id",
                (
                    SELECT
                        "id"
                    FROM
                        "abyssal_modules_typeattribute"
                    WHERE
                        "attribute_id" = 10977 AND
                        "type_id" = "_type_id"
                ) AS "new_attribute_id"
            FROM
                abyssal_modules_attributes__view
            WHERE
                _attribute_id = 977;
            """,
            reverse_sql="DROP VIEW IF EXISTS abyssal_modules_derived_attributes__view;"
        )
    ]
