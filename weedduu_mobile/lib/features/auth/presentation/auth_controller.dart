import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:weedduu_mobile/features/auth/data/auth_repository.dart';
import 'package:weedduu_mobile/features/auth/providers/auth_provider.dart';
import '../../../core/services/secure_storage_service.dart';

final authControllerProvider = Provider((ref) {
  final repo = ref.watch(authRepositoryProvider);
  return AuthController(ref: ref, repo: repo);
});

class AuthController {
  final Ref ref;
  final AuthRepository repo;
  final SecureStorageService _storage = SecureStorageService();

  AuthController({required this.ref, required this.repo});

  Future<bool> login(String email, String password) async {
    final user = await repo.login(email, password);
    if (user != null) {
      await _storage.saveToken(user.token);
      ref.read(userProvider.notifier).state = user;
      return true;
    }
    return false;
  }

  Future<bool> register(String email, String password) async {
    final user = await repo.register(email, password);
    if (user != null) {
      await _storage.saveToken(user.token);
      ref.read(userProvider.notifier).state = user;
      return true;
    }
    return false;
  }

  Future<void> logout() async {
    await _storage.deleteToken();
    ref.read(userProvider.notifier).state = null;
  }
}
