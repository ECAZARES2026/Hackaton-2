from pathlib import Path
import shutil


MODELO_ACTUAL = Path("modelo.pkl")
MODELO_BACKUP = Path("modelo_backup.pkl")


def ejecutar_rollback() -> None:
    if not MODELO_BACKUP.exists():
        raise FileNotFoundError(
            "No se encontró modelo_backup.pkl"
        )

    shutil.copy2(
        MODELO_BACKUP,
        MODELO_ACTUAL
    )

    print("ROLLBACK EJECUTADO CORRECTAMENTE")
    print("modelo.pkl fue restaurado desde modelo_backup.pkl")


if __name__ == "__main__":
    ejecutar_rollback()