// core/services/secure_storage_service.dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStorageService {
  final _storage = const FlutterSecureStorage();

  Future<void> saveToken(String token) async =>
      await _storage.write(key: 'token', value: token);

  Future<String?> getToken() async => await _storage.read(key: 'token');

  Future<void> deleteToken() async => await _storage.delete(key: 'token');
}
