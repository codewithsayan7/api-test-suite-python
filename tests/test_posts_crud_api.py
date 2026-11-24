def test_create_post_returns_201(api):
    payload = {
        "title": "QA automation check",
        "body": "Verifying POST /posts endpoint",
        "userId": 1,
    }
    resp = api.post("/posts", payload)

    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == 1
    assert "id" in data


def test_update_post_returns_200(api):
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated content",
        "userId": 1,
    }
    resp = api.put("/posts/1", payload)

    assert resp.status_code == 200
    assert resp.json()["title"] == "Updated title"


def test_delete_post_returns_200(api):
    resp = api.delete("/posts/1")
    assert resp.status_code == 200


def test_filter_posts_by_user_id(api):
    resp = api.get("/posts", params={"userId": 2})

    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) > 0
    assert all(p["userId"] == 2 for p in posts)
