import pytest
from great_expectations.data_context import DataContext
from great_expectations.core.batch import BatchRequest

@pytest.fixture(scope="module")
def ge_context():
    return DataContext()

def test_dbt_model_output(ge_context):
    #指定驗證的相關資料
    batch_request = BatchRequest(
        datasource_name="dbt_datasource",
        data_connector_name="default_inferred_data_connector_name",
        data_asset_name="my_dbt_table", 
        batch_identifiers={"default_identifier_name": "default_identifier"}
    )
    
    # 指定要使用的預期檢查
    expectation_suite_name = "my_dbt_table_suite"
    
    # 取得檢查
    validator = ge_context.get_validator(
        batch_request=batch_request, expectation_suite_name=expectation_suite_name
    )
    
    # 檢查和確認結果
    results = validator.validate()
    assert results["success"] is True, "數據未通過 Great Expectations 驗證"