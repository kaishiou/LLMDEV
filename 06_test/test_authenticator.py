# 06_test/test_authenticator.py
import pytest
from authenticator import Authenticator


class TestAuthenticator:
    def setup_method(self):
        # 各テストは独立させるため、毎回新しいインスタンスを作成
        self.auth = Authenticator()

    def test_register_user_success(self):
        """register() でユーザーが正しく登録されるか"""
        self.auth.register("alice", "password123")
        assert "alice" in self.auth.users
        assert self.auth.users["alice"] == "password123"

    def test_register_user_already_exists(self):
        """既存ユーザー名で登録しようとすると ValueError が出るか（メッセージも検証）"""
        self.auth.register("bob", "secret")
        with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
            self.auth.register("bob", "anotherpass")

    def test_login_success(self):
        """正しいユーザー名とパスワードでログインできるか"""
        self.auth.register("charlie", "mypassword")
        result = self.auth.login("charlie", "mypassword")
        assert result == "ログイン成功"

    def test_login_wrong_password(self):
        """誤ったパスワードでログインすると ValueError が出るか（メッセージも検証）"""
        self.auth.register("dave", "correctpw")
        with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
            self.auth.login("dave", "wrongpw")
