import sys
from .app import MangoSettings

def main():
    app = MangoSettings()
    return app.run(sys.argv)

if __name__ == "__main__":
    main()