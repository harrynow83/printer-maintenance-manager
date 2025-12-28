
---

## 4️⃣ `docs/MAINTENANCE_PRESETS.md`

### 📌 Para quién es
👉 Usuarios que quieren entender los intervalos  
👉 Buenas prácticas

---

### 📄 CONTENIDO (COPIAR Y PEGAR)

```md
# Maintenance Presets

Default maintenance tasks are based on common 3D printer usage.

## Default Tasks

| Task | Interval (hours) | Description |
|----|------------------|------------|
| nozzle_clean | 100 | Clean nozzle and check extrusion |
| belts_check | 300 | Check belt tension |
| lubrication | 500 | Lubricate axes |
| hotend_overhaul | 1000 | Full hotend inspection |

## Customization

You can change intervals in `config.yaml`:

```yaml
maintenance:
  nozzle_clean: 80
  belts_check: 250
