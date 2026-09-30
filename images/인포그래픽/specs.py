import json
BG="#F7F5F0"
TH="theme\n  palette {pal}\n  base\n    text\n      font-family IBM Plex Sans KR"
P4="#16213A #C8412B #2F5D8A #B7791F"
def th(p=P4): return TH.format(pal=p)
def items(key, rows):
    s=f"  {key}\n"
    for r in rows:
        lab,desc,icon=r[0],r[1],r[2]
        s+=f"    - label {lab}\n"
        if desc: s+=f"      desc {desc}\n"
        if icon: s+=f"      icon ref:mi:{icon}\n"
    return s
def vals(rows):
    s="  values\n"
    for l,v in rows: s+=f"    - label {l}\n      value {v}\n"
    return s
def tree(node, ind=4):
    lab,icon,ch=node; p=" "*ind
    s=f"{p}label {lab}\n"+(f"{p}icon ref:mi:{icon}\n" if icon else "")
    if ch:
        s+=f"{p}children\n"
        for c in ch: s+=f"{p}  - "+tree(c, ind+4)[ind+4:]
    return s
S=[]
def add(name,tpl,body,w=1110,h=420,pal=P4): S.append({"name":name,"w":w,"h":h,"bg":BG,"dsl":f"infographic {tpl}\ndata\n{body}{th(pal)}"})
# Ⅰ
add("gdp-per-capita","chart-column-simple",vals([("일본",35703),("한국",37412)]),600,420,"#C8412B #2F5D8A")
add("industry","list-grid-badge-card",items("lists",[("제조업 수출 경제","자동차·반도체 장비·로봇·소재","factory-fill"),("대기업 주도","스타트업 투자 대기업 400개사+","building-2-fill"),("사업화 부진","연구력 세계 1위, 유니콘은 적음","bulb-fill"),("인력 부족","65세 이상 29.6%","user-3-fill"),("전략 투자 재편","17개 전략 분야 집중","target-fill"),("스타트업 과제","8개 분야횡단 과제 중 하나","rocket-fill")]),1110,440)
add("startups","chart-column-simple",vals([("2021",16100),("2025",25000)]),520,420,"#9AA3B2 #C8412B")
add("univ","chart-column-simple",vals([("2021년도",3305),("2024년도",5074)]),520,420,"#9AA3B2 #2F5D8A")
add("funding","chart-column-simple",vals([("2024 속보",7793),("2024 보정",8828),("2025 속보",7613),("2026 상반기",3779)]),1000,440,"#9AA3B2 #16213A #C8412B #B7791F")
add("target-gap","chart-bar-plain-text",vals([("2027년도 목표",100000),("2025년 실적(속보)",7613)]),1000,300,"#16213A #C8412B")
add("vc-source","chart-pie-donut-pill-badge",vals([("은행·신용금고",35.8),("사업법인",25.1),("연기금",2.6),("그 외",36.5)]),820,440,"#16213A #C8412B #B7791F #C9CED6")
add("tokyo-share","chart-pie-donut-plain-text",vals([("도쿄",77.2),("도쿄 외",22.8)]),560,420,"#C8412B #C9CED6")
add("exit","chart-column-simple",vals([("2024 IPO",49),("2025 IPO",31)]),520,420,"#9AA3B2 #C8412B")
# Ⅱ
add("policy-flow","list-row-horizontal-icon-arrow",items("lists",[("2022.11","5개년 계획","flag-2-fill"),("2025.11","성장전략본부 설치","bank-fill"),("2026.05","총력창출 패키지","rocket-fill"),("2026.07","일본성장전략","trending-up-fill")]),1110,420)
add("package","list-grid-ribbon-card",items("lists",[("① 스케일업","성장자금·엑시트·글로벌",None),("② 딥테크","정부·대기업 조달, SBIR 강화",None),("③ 지역","기업가 교육·고센·지자체 조달",None)]),1110,300,"#16213A #C8412B #2F5D8A")
add("targets","list-grid-badge-card",items("lists",[("투자 10조 엔","2027년도, 2022년도의 10배","coin-fill"),("유니콘 100개","장래 목표","star-fill"),("스타트업 10만 개","장래 목표","rocket-fill")]),1110,260,"#16213A #C8412B #2F5D8A")
add("tax","list-grid-badge-card",items("lists",[("엔젤세제","재투자·직접 창업 시 최대 20억 엔 비과세","pig-money-fill"),("스톡옵션 세제","연간 행사 한도 최대 3,600만 엔","certificate-fill"),("오픈이노베이션 세제","스타트업 출자·M&A 시 25% 소득공제","link-fill")]),1110,300,"#16213A #C8412B #2F5D8A")
add("sbir","list-row-horizontal-icon-arrow",items("lists",[("페이즈1·2","부처 과제 연구개발","flask-fill"),("페이즈3","대규모 실증 2,060억 엔","chart-bar-fill"),("정부조달","시험 도입 → 본격 조달","bank-fill")]),1110,400,"#16213A #C8412B #2F5D8A")
add("org","hierarchy-tree-tech-style-badge-card","  root\n"+tree(("일본성장전략본부","bank-fill",[("경제산업성","factory-fill",[("NEDO",None,None),("JETRO",None,None),("IPA",None,None)]),("내각부","building-2-fill",[("SBIR 조정",None,None)]),("문부과학성","school-fill",[("JST",None,None)]),("중소기업청","store-fill",[("SMRJ",None,None)]),("재무성","coin-fill",[("JFC",None,None)])])),1110,460)
add("directions","list-grid-badge-card",items("lists",[("민간 주도·마중물","세제·규제개혁·펀드 출자·인증","hand-heart-fill"),("스케일업","성장자금 공급 최우선","trending-up-fill"),("딥테크 집중","17개 전략 분야 일관 지원","flask-fill"),("정부조달 수요","R&D → 시험 도입 → 조달","bank-fill"),("지역 확산","거점도시 13개·지자체 조달","map-pin-fill"),("글로벌 양면성","문호 개방 + 재류자격 적정화","earth-fill")]),1110,440)
# Ⅲ
add("pathway","sequence-ascending-steps",items("sequences",[("교육 이수","특정창업지원",None),("공적 인증","시정촌 증명서",None),("정책융자","JFC 최대 7,200만 엔",None),("소액 보조금","지속화 최대 200만 엔",None),("VC 매칭","딥테크 DTSU 최대 30억 엔",None)]),1110,440,"#9AA3B2 #2F5D8A #16213A #B7791F #C8412B")
add("scale","chart-bar-plain-text",vals([("지속화보조금",200),("NEP 개척",300),("미토",302.4),("도쿄도 창업조성",400),("NEP 약진",3000),("JFC 융자",7200)]),1000,420,"#16213A")
add("tokutei","hierarchy-tree-tech-style-badge-card","  root\n"+tree(("시정촌 증명서","certificate-fill",[("등록면허세 절반","file-certificate-fill",None),("신용보증 6개월 전","safe-shield-fill",None),("JFC 특별금리","coin-fill",None),("지속화보조금 자격","wallet-fill",None)])),1110,380)
add("jfc","chart-column-simple",vals([("국민생활사업",7200),("운전자금 한도",4800)]),560,420,"#16213A #2F5D8A")
add("nep","list-grid-badge-card",items("lists",[("개척코스","창업 전 개인·팀 · 월 25만 엔, 최대 300만 엔","user-3-fill"),("약진코스","중소 법인 · 최대 500만 또는 3,000만 엔","rocket-fill")]),900,220,"#2F5D8A #C8412B")
add("mitou","list-row-horizontal-icon-arrow",items("lists",[("선발","25세 미만 개인·그룹","user-star-fill"),("PM 지도","톱 러너 PM 조언","user-follow-fill"),("프로젝트","최대 302.4만 엔·9개월","wallet-fill"),("창업·사업화","수료생 약 500명","rocket-fill")]),1110,400)
add("tokyo","chart-pie-donut-plain-text",vals([("도쿄도 보조",66.7),("자부담",33.3)]),520,400,"#C8412B #C9CED6")
add("visa-steps","list-row-horizontal-icon-arrow",items("lists",[("사업계획서","인정 실시단체 제출","file-fill"),("확인서","지자체·단체 발급","file-check-fill"),("재류자격","입관 특정활동 44호","passport-fill"),("창업 준비","최장 2년","time-fill"),("전환","경영·관리 비자","idcard-fill")]),1110,400,"#16213A #2F5D8A #B7791F #C8412B #16213A")
add("dtsu-match","chart-pie-donut-pill-badge",vals([("VC 등 출자",33.3),("NEDO 보조",66.7)]),600,420,"#B7791F #16213A")
add("dtsu-phase","sequence-ascending-steps",items("sequences",[("STS","실용화 전기 3억·5억 엔",None),("PCA","후기 5억·10억 엔",None),("DMP","양산 실증 25억 엔",None)]),1000,400,"#2F5D8A #16213A #C8412B")
add("jizoku","chart-column-simple",vals([("일반형",50),("창업형",200),("인보이스 특례",250)]),640,420,"#9AA3B2 #C8412B #B7791F")
add("jstartup","chart-column-simple",vals([("전국판",270),("CENTRAL",55)]),560,420,"#16213A #C8412B")
add("features","list-grid-badge-card",items("lists",[("인증 연결형","증명서가 세제·보증·융자 우대로","certificate-fill"),("보조금보다 융자","주력은 JFC 최대 7,200만 엔","coin-fill"),("개인 선발형","법인 설립 전 ‘사람’ 선발","user-star-fill"),("딥테크는 대형","VC 매칭 최대 30억 엔","flask-fill"),("지자체 보조금","사업화 현금은 지자체 몫","map-pin-fill"),("TIPS 비교 = DTSU","J-Startup은 인증 제도","link-fill")]),1110,440)
# Ⅳ
add("visa-capital","chart-column-simple",vals([("개정 전",500),("개정 후",3000)]),560,420,"#9AA3B2 #C8412B")
add("foreign-drop","chart-column-simple",vals([("2025 상반기",9851),("2026 상반기",4731)]),560,420,"#9AA3B2 #C8412B")
add("foreign-prog","list-grid-badge-card",items("lists",[("스타트업 비자","창업 준비 최장 2년","passport-fill"),("J-Find","해외 명문대 졸업자 최장 2년","school-fill"),("JEAP","진입 가속·대기업 매칭","rocket-fill"),("IBSC","무료 임시 사무실 50영업일","building-1-fill"),("J-Bridge","오픈이노베이션 매칭","link-fill"),("지자체 창구","설립·생활·자금 원스톱","map-pin-fill")]),1110,440)
add("promising","list-grid-badge-card",items("lists",[("AI·피지컬 AI","전략 분야 1순위·GENIAC","ai-fill"),("헬스케어·의료 AI","고령화율 29.6%","heartbeat-fill"),("DX·SaaS·성력화","인력 부족","robot-fill"),("GX·탈탄소","JEAP 탈탄소 트랙","leaf-fill"),("방위·듀얼유즈","디펜스테크 SBIR","shield-fill"),("콘텐츠·소비재","콘텐츠·푸드테크","film-fill")]),1110,440)
add("conditions","list-row-horizontal-icon-arrow",items("lists",[("체류·비자","자본금 3,000만 엔 등 신기준","passport-fill"),("법인·은행 계좌","계좌 개설이 별도 병목","bank-card-fill"),("인력·언어","상근직원 1명·일본어 B2","user-3-fill"),("상관행","대면·신뢰, 긴 리드타임","handshake-fill" if False else "hand-heart-fill"),("세무","인보이스 제도 사전 확인","file-fill")]),1110,400)
# Ⅴ
add("kr-budget","chart-pie-donut-pill-badge",vals([("융자",41.1),("기술개발",25.0),("사업화",23.5),("그 외",10.4)]),820,440,"#2F5D8A #16213A #C8412B #C9CED6")
add("kr-invest","chart-column-simple",vals([("2025 연간",69358),("2026 상반기",78005)]),560,420,"#9AA3B2 #2F5D8A")
add("kr-stages","sequence-ascending-steps",items("sequences",[("예비창업패키지","최대 1억 원",None),("초기창업패키지","3년 이내, 최대 1억 원",None),("창업도약패키지","3~7년, 최대 2억 원",None)]),1000,400,"#9AA3B2 #2F5D8A #16213A")
add("unicorn-cmp","chart-column-simple",vals([("일본",9),("한국",16)]),520,420,"#C8412B #2F5D8A")
add("deeptech-cmp","chart-column-simple",vals([("TIPS 딥테크(억 원)",15),("DTSU(억 엔)",30)]),560,420,"#2F5D8A #C8412B")
json.dump(S,open("specs.json","w"),ensure_ascii=False)
print(len(S))
