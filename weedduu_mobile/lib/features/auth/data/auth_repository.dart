// features/auth/data/auth_repository.dart
import '../../../core/services/api_service.dart';
import '../domain/user_model.dart';

class AuthRepository {
  final _api = ApiService();

  Future<User?> login(String email, String password) async {
    final response = await _api.post('/users/login/', {
      'email': email,
      'password': password,
    });

    if (response.statusCode == 200) {
      return User.fromJson(response.data);
    }
    return null;
  }

  Future<User?> register(String email, String password) async {
    final response = await _api.post('/users/sign-up/', {
      'email': email,
      'password': password,
    });

    if (response.statusCode == 201) {
      return User.fromJson(response.data);
    }
    return null;
  }
}
