from playwright.sync_api import Playwright

def test_get_user(playwright: Playwright):
    #create API context
    api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")

    #send GET request
    response = api.get("/users/1")

    #assert status code
    assert response.status == 200

    # parse response body
    body = response.json()

    #assert specific fields
    assert body["id"] == 1
    assert body["name"] == "Leanne Graham"
    assert body["email"] == "Sincere@april.biz"

    #print response
    #print(response.json())

def test_create_post(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")

    response = api.post("/posts", data={
        "title": "QA Automation",
        "body": "Playwright is awesome",
        "userId": 1
    })
    
    assert response.status == 201   # what status code means "created"?
    body = response.json()
    assert body["title"] == "QA Automation"

def test_delete_post(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api.delete("/posts/1")
    assert response.status == 200   # what status means successful delete?    