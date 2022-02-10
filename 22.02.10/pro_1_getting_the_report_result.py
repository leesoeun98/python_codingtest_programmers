def solution(id_list, report, k):
    sreport = list(set(report))
    reportcount = {name: 0 for name in id_list}
    reportname = {name: [] for name in id_list}
    res = {name: 0 for name in id_list}

    for r in sreport:
        user = r.split(' ')[0]
        bad = r.split(' ')[1]
        reportcount[bad] += 1
        reportname[user].append(bad)

    blocked = list(key for key, value in reportcount.items() if value >= k)

    for k, v in reportname.items():
        for b in blocked:
            if b in v:
                res[k] += 1
    return list(value for key, value in res.items())
