// core/services/api_service.dart
import 'package:dio/dio.dart';
import 'secure_storage_service.dart';
import '../config/api_config.dart';

class ApiService {
  late Dio dio;
  final SecureStorageService _storageService = SecureStorageService();

  ApiService() {
    dio = Dio(BaseOptions(baseUrl: baseUrl))
      ..interceptors.add(
        InterceptorsWrapper(
          onRequest: (options, handler) async {
            final token = await _storageService.getToken();
            if (token != null) {
              options.headers['Authorization'] = 'Bearer $token';
            }
            return handler.next(options);
          },
        ),
      );
  }

  Future<Response> post(String path, Map<String, dynamic> data) async {
    return await dio.post(path, data: data);
  }

  Future<Response> get(String path) async {
    return await dio.get(path);
  }
}
