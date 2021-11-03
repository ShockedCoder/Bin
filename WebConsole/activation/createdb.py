import importlib.util as imp

spec = imp.spec_from_file_location("main", "main.py")
main = imp.module_from_spec(spec)
spec.loader.exec_module(main)

main.db.create_all()