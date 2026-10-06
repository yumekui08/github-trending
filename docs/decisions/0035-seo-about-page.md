# 0035 検索に出るようにする：説明のページ、詳しいページの題と構造化データ、404、Search Console

- 日付：2026-10-07
- 状態：決定（0026 の詳しいページの題を改める）

## 背景
本人から、サイトを検索に出るようにしたい、と。特に、各リポジトリの詳しいページは検索に出る状態にしたい。また、サイトが何で、どういうサービスかを説明するページを作り、それも検索の入り口にしたい。Google Search Console で扱えるよう、所有確認のタグ（`google-site-verification`）を入れたい。値は環境変数で設定できるようにする。

0027 で、description・canonical・OGP・sitemap・robots.txt・フィードはすでに出している。

## 決定
- **所有確認のタグ**：環境変数 `GOOGLE_SITE_VERIFICATION` に値があれば、全ページの `<head>` に `<meta name="google-site-verification" content="値">` を出す。なければ出さない。手元は `.env`、Actions は Variables（Settings → Secrets and variables → Actions → Variables）の `GOOGLE_SITE_VERIFICATION` を `daily.yml` の「HTML を作る」に渡す。HTML に出る値で秘密ではないので、Secrets ではなく Variables に置く。どちらに登録しても動くよう、Variables になければ Secrets の同じ名前から読む。`build` は確認のタグを出したかどうかをログに1行出す（値は出さない）
- **説明のページ `/about/`**：題は「github新聞とは｜GitHub Trending を毎朝日本語で要約」。何のサイトか、なぜ作ったか、読めるもの、作り方（取得 → 材料集め → AI の要約 → 公開）と要約の決まり、紙面の見方、注意（AI の要約で誤りがありうる、GitHub とは無関係）、これまでの件数、最近の解説6件。全ページのフッターから入れる。sitemap に載せる
  - URL は `/welcome/` や `/home/` ではなく、こうしたページで広く使われる `/about/` にした
  - トップ（`/`）の題は 0026 のとおり「github新聞」のまま。説明の言葉は `/about/` が受け持つ
- **詳しいページ**
  - 題を「owner/name とは：what | github新聞」にする（「〇〇 とは」で探す人に見つけてもらうため。リポジトリ名は先頭のままなので、タブで見分けられる）
  - 構造化データ（JSON-LD）：`TechArticle`（見出し、説明、要約した日、著者、発行元、`about` に `SoftwareSourceCode` としてリポジトリの URL と言語）と、パンくず（`BreadcrumbList`）。絶対 URL が要るので `site_base_url` があるときだけ
  - `article:published_time`・`article:modified_time`・`article:tag` を出す
  - ページの末尾に「同じ分野の記事」：先頭のタグが同じほかのリポジトリの解説を、要約した日の新しい順に5件。ページどうしがつながり、検索エンジンがたどりやすくなる。判断は入らない
- **トップ**：構造化データ `WebSite` を出す
- **404 ページ**：Cloudflare Pages は `404.html` がないと、ない URL にもトップを 200 で返す（検索エンジンからは中身の重複に見える）。`404.html` を作り、`noindex` を付け、トップ・過去の日・説明のページへのリンクを置く。どの深さの URL でも出るので、リンクはサイトの根からの絶対パス。canonical は出さない

## 本人がやること
- GitHub の Variables に `GOOGLE_SITE_VERIFICATION` を登録する（登録してから次にサイトを作り直したときに、タグが出る）
- Search Console で所有を確認したら、`https://github-trending.yumekui.org/sitemap.xml`（0036 で独自ドメインに） を「サイトマップ」に登録する
