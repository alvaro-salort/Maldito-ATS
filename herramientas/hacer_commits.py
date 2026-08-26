import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

def run_git(args: list[str]):
    cmd = ["git"] + args
    print(f">> git {' '.join(args)}")
    res = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr and res.returncode != 0:
        print(f"Error: {res.stderr.strip()}", file=sys.stderr)
    return res

# 1. Inicializar git si no existe
run_git(["init", "-b", "main"])

# 2. Configurar remote origin
run_git(["remote", "remove", "origin"])
run_git(["remote", "add", "origin", "https://github.com/alvaro-salort/Maldito-ATS.git"])

# 3. Eliminar archivos temporales
temp_files = [RAIZ / "herramientas" / "renombrar_proyecto.py", RAIZ / "herramientas" / "limpiar_legado.py"]
for tf in temp_files:
    if tf.exists():
        tf.unlink()

# Commit 1: Estructura base y documentación inicial
run_git(["add", ".gitignore", "LICENSE", "README.md", "INICIO_RAPIDO.md", "HISTORIAL_CAMBIOS.md", "requirements.txt"])
run_git(["commit", "-m", "chore: inicializar repositorio, documentacion base y dependencias"])

# Commit 2: Configuración multi-agente
run_git(["add", "AGENTS.md", "OPENCODE.md", "CLAUDE.md", ".claude/settings.json", ".opencode/settings.json"])
run_git(["commit", "-m", "feat(agentes): configuracion agnostica para OpenCode, Claude y modelos libres"])

# Commit 3: Metodología del asistente y habilidades
run_git(["add", ".claude/skills/", ".claude/agents/"])
run_git(["commit", "-m", "feat(skills): metodologia de evaluacion, redaccion y perfil del candidato"])

# Commit 4: Portales de búsqueda de empleo regionales
run_git(["add", ".agents/skills/busqueda-bumeran/", ".agents/skills/busqueda-computrabajo/", ".agents/skills/busqueda-getonbrd/", ".agents/skills/busqueda-linkedin/", ".agents/skills/busqueda-remota/"])
run_git(["commit", "-m", "feat(portales): herramientas de busqueda para Argentina y LATAM"])

# Commit 5: ResumeSkills y networking
run_git(["add", ".agents/skills/redactor-vinietas/", ".agents/skills/optimizador-linkedin/", ".agents/skills/mensajes-networking/", ".agents/skills/comparador-ofertas/", "plantillas/"])
run_git(["commit", "-m", "feat(resumeskills): formula XYZ, optimizador de LinkedIn y networking"])

# Commit 6: Comandos interactivos
run_git(["add", ".opencode/commands/", ".claude/commands/"])
run_git(["commit", "-m", "feat(comandos): comandos interactivos en espanol para el asistente"])

# Commit 7: Herramientas Python y tests
run_git(["add", "herramientas/", "pruebas/"])
run_git(["commit", "-m", "feat(herramientas): motor salarial Sysarmy, validador ATS y tests"])

# Commit 8: Plantillas LaTeX y carpetas de trabajo
run_git(["add", "cv/", "cartas_presentacion/", "documentos/", "buscador_empleos/", "investigacion_empresas/", "capacitacion/"])
run_git(["commit", "-m", "feat(plantillas): plantillas LaTeX de CV, cartas y carpetas de trabajo"])

# Estado final
print("\n=== HISTORIAL DE COMMITS CREADO ===")
run_git(["log", "--oneline", "-n", "10"])

print("\n=== PUSH A GITHUB ===")
push_res = run_git(["push", "-u", "origin", "main"])
if push_res.returncode == 0:
    print("✅ Repositorio subido exitosamente a https://github.com/alvaro-salort/Maldito-ATS")
else:
    print("⚠️ El push requiere autenticación o permisos. Podés ejecutar 'git push -u origin main' en tu terminal.")
