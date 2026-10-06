# 0036 公開先を独自ドメイン github-trending.yumekui.org にする

- 日付：2026-10-07
- 状態：決定（0028 の「独自ドメインに移ったら `site_base_url` を直す」を実行した）

## 背景
本人が Cloudflare Pages のプロジェクト `trending-digest` に独自ドメイン `github-trending.yumekui.org` を付けた。サイトはそちらで見られるが、`config.yaml` の `site_base_url` が `https://trending-digest.pages.dev/` のままで、canonical・OGP・sitemap・フィード・Discord の通知のリンクが古い URL を指していた。検索に出す（0035）には、検索エンジンに正しい URL を伝える必要がある。

## 決定
- `config.yaml` の `site_base_url` を `https://github-trending.yumekui.org/` にする。canonical・og:url・og:image・sitemap・robots.txt・フィード・構造化データ・Discord の通知のリンクが、すべて新しいドメインになる
- Cloudflare Pages のプロジェクト名は `trending-digest` のまま（`daily.yml` の公開先も変えない）。`https://trending-digest.pages.dev/` でも同じページが見えるが、どのページも canonical で新しいドメインを指すので、検索エンジンは新しいドメインの方を載せる

## 影響
- フィードの記事の ID は URL から作っている（0027）ので、RSS リーダーによっては、今までの記事がもう一度「新しい記事」として出ることがある（1回だけ）
- pages.dev から新しいドメインへ転送したいときは、Cloudflare の Bulk Redirects で設定する（コードでは扱わない）
