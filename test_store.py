import uuid

from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.mark.parametrize("order_id , payload" , [(101, {"order_status": "shipped", "pet_staus" : "sold"})])
def test_patch_order_by_id(order_id, payload):
    pass
    test_endpoint_patch = "/store/order/{order_id}"
    res = api_helpers.patch_api_data(test_endpoint_patch, payload)
    assert res.status_code == 200
    validate(instance=res.json(), schema=schemas.pet)
    return res
    expected_msg = "Order and pet status updated successfully"
    assert_that(res.json(), contains_string(expected_msg))







