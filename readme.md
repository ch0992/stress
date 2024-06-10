# stress test를 위한 fastapi 및 locust practice



# 1. set environment

### 1) requires
python, pip

### 2) fastapi 설치
```
pip install fastapi
pip install uvicorn
```

### 3) locust 설치
```
pip install locust
```

### 4) fastapi 실행

```
fastapi dev .\practice\fastapi\step2.py
```

### 5) locust 실행

```
locust -f .\practice\locust\locusfile_2.py
```






---

# references
  
1. fastapi 설치
https://velog.io/@munang/Python-FastAPI-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0

2. locust 설치
https://wookkl.tistory.com/67


3. locust stress test
https://github.com/salgieri/rasa-locust-stress-test
https://github.com/janneri/locust-tutorial
https://github.com/Curt-Park/locust-k8s
https://github.com/BatuhanKucukali/locust-example


4. auto load test
https://github.com/silverstone1903/auto-load-testing
https://github.com/hkiang01/autoloadtest


4. iperf3 를 이용한 네트워크 테스트
https://medium.com/@muthanagavamsi/kubernetes-network-bandwidth-test-between-2-pods-a01a154ba07f



