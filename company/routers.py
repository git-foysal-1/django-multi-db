class CompanyRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'company':
#             return f'company_{model.name}'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'company':
#             return f'company_{model.name}'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label == 'company' or
#             obj2._meta.app_label == 'company'
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'company':
#             return db == f'company_{model_name}'
#         return None
    pass 