from locust import HttpUser, task, between

# FastAPIUser 클래스는 Locust의 HttpUser 클래스를 상속받아 테스트 사용자 시뮬레이션을 정의합니다.
class FastAPIUser(HttpUser):
    # 사용자 시뮬레이션 간의 대기 시간을 설정합니다. 여기서는 각 요청 간의 대기 시간이 1초에서 5초 사이로 설정됩니다.
    wait_time = between(1, 5)

    # 호스트 URL을 지정합니다. 이 예제에서는 로컬에서 실행 중인 FastAPI 서버의 주소입니다.
    host = "http://127.0.0.1:8000"

    # Path 파라미터만 포함한 GET 요청을 테스트하는 작업
    @task
    def get_item_with_path_param(self):
        # /items/1 엔드포인트에 GET 요청을 보냅니다.
        self.client.get("/items/1")

    # Query string만 포함한 GET 요청을 테스트하는 작업
    @task
    def get_item_with_query_string(self):
        # /items 엔드포인트에 name과 description query string을 포함한 GET 요청을 보냅니다.
        self.client.get("/items?name=Test+Item&description=This+is+a+test+item")

    # Path 파라미터와 query string을 모두 포함한 GET 요청을 테스트하는 작업
    @task
    def get_item_with_path_and_query(self):
        # /items/1 엔드포인트에 name과 description query string을 포함한 GET 요청을 보냅니다.
        self.client.get("/items/1?name=Test+Item&description=This+is+a+test+item")

    # POST 요청을 테스트하는 작업
    @task
    def create_item(self):
        # /items/ 엔드포인트에 POST 요청을 보냅니다.
        # 요청 본문으로 JSON 형식의 데이터를 전송합니다.
        self.client.post("/items/", json={"name": "Test Item", "description": "This is a test item"})
