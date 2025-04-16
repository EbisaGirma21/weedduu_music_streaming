// features/auth/provider/auth_provider.dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:weedduu_mobile/features/auth/data/auth_repository.dart';
import 'package:weedduu_mobile/features/auth/domain/user_model.dart';

final authRepositoryProvider = Provider((ref) => AuthRepository());
final userProvider = StateProvider<User?>((ref) => null);
