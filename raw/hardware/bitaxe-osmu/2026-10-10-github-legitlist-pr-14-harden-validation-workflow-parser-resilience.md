# bitaxeorg/legitlist pull request #14: Harden validation workflow and parser resilience

> Source: https://github.com/bitaxeorg/legitlist/pull/14
> Collected: 2026-10-10
> Published: 2026-03-20
> Registry ID: legitlist

- Repository: bitaxeorg/legitlist
- Type: pull request
- Number: 14
- State: closed, MERGED 2026-03-20T15:24:17Z
- Author: DerekLoadout
- Opened: 2026-03-20
- Files: .github/pull_request_template.md (+1/-1), .github/workflows/validate-vendor.yml (+6/-98), scripts/validate-all.mjs (+8/-1)

## Body

> ## Summary
> - make CI run the same repository validator used locally (npm run validate)
> - add graceful JSON parse error handling in scripts/validate-all.mjs so malformed files are reported without crashing the run
> - clarify allowed region values directly in the PR template to reduce avoidable submission errors
>
> ## Why
> This removes validation drift between local and CI checks, avoids brittle workflow dependencies, and makes contributor instructions more explicit.

## Key patches

.github/workflows/validate-vendor.yml — the entire ~92-line inline shell validator (ajv-cli + jq + stat logic checking schema/slug/logo/size) was deleted and replaced by the repo's own npm validator; this hunk pair is the whole story (verbatim):

```yaml
-      - name: Install validators
-        run: npm install -g ajv-cli@5.0.0 ajv-formats@3.0.1
+      - name: Install dependencies
+        run: npm ci
+          cache: npm
```

```yaml
+      - name: Run repository validator
+        run: npm run validate
```

(The deleted block included the logo ≤ 200 KB check, slug=filename check, logo-exists check — these now live in scripts/validate-all.mjs.)

scripts/validate-all.mjs — graceful parse handling (verbatim hunk):

```js
-  const data = JSON.parse(fs.readFileSync(filePath, "utf-8"))
+  let data
+  try {
+    data = JSON.parse(fs.readFileSync(filePath, "utf-8"))
+  } catch (err) {
+    console.error(`❌ ${file} — Invalid JSON: ${err.message}`)
+    errors++
+    continue
+  }
```

PR template — region field pinned to the seven allowed values (verbatim):

```markdown
-| **Region** | Your region |
+| **Region** | Europe / North America / South America / Asia Pacific / Middle East / Africa / India |
```
