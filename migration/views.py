from django.shortcuts import render

def index(request):
  limit = int(request.GET.get("limit", 3))
  data = {"web": (2, 2), "db": (1, 5), "api": (3, 4), "backup": (1, 1)}
  rows = [(s, a, b, "стоп" if b > limit else "ок") for s, (a, b) in data.items()]
  stop = sum(1 for r in rows if r[3] == "стоп")
  return render(request, "index.html", {
      "limit": limit, "rows": rows, "names": list(data),
      "before": [v[0] for v in data.values()],
      "after": [v[1] for v in data.values()],
      "stop": stop, "ok": len(rows) - stop,
  }) 