# Phone Skills contributors

- Keep shared call mechanics in `skills/skysay-phone/references/phone-tasks.md` and workspace/campaign mechanics in that skill's other references. Specialties add task-specific decisions and evidence.
- Every skill needs a concise `name` and `description` in SKILL.md and matching `agents/openai.yaml` metadata. Keep normal automatic discovery enabled.
- Read current tool schemas before adding request examples. Never invent a tool, field, supported language, price or server-enforced approval guarantee.
- Preserve explicit authorization and exact-request idempotency. Reconcile both uncertain submissions and possible business commitments before retrying.
- Keep a configuration save, campaign launch, simulation, answered call and confirmed business result distinct. Claim real-call qualification only with recorded evidence.
- Do not store credentials, customer data or private recordings here. Repository validation does not authorize paid calls or production routing changes.
- Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests` after changes. Behavioral review is separate from structural validation.
