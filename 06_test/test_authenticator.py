from collections.abc import Iterator
import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator() -> Iterator[Authenticator]:
  auth = Authenticator()
  auth.register('name', 'pass')
  yield auth

def test_register_normal(authenticator: Authenticator) -> None:
  assert 'name' in authenticator.users

def test_register_already_exists_user(authenticator: Authenticator) -> None:
  with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
    authenticator.register('name', 'password')

def test_login_normal(authenticator: Authenticator) -> None:
  assert authenticator.login('name', 'pass') == 'ログイン成功'

def test_login_unmatch_password(authenticator: Authenticator) -> None:
  with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
    authenticator.login('name', '')
