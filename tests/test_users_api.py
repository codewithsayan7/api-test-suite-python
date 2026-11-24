import pytest


REQUIRED_USER_KEYS = {"id", "name", "username", "email", "address", "company"}


def test_list_users_returns_200_and_valid_schema(api):
    resp = api.get("/users")

    assert resp.status_code == 200
    assert resp.elapsed.total_seconds() < 3.0

    users = resp.json()
    assert len(users) == 10
    for user in users:
        assert REQUIRED_USER_KEYS.issubset(user.keys())
        assert "@" in user["email"]


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_single_user_by_id(api, user_id):
    resp = api.get(f"/users/{user_id}")

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == user_id
    assert body["name"]


@pytest.mark.parametrize("invalid_id", [0, 9999, "abc"])
def test_get_nonexistent_user_returns_404(api, invalid_id):
    resp = api.get(f"/users/{invalid_id}")
    assert resp.status_code == 404
