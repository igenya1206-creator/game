# COSTUME SELECT

キャラクターの衣装を切り替えてプレビューするアプリ。

## 構成
- `index.html` / `styles.css` / `app.js` — アプリ本体
- `assets/base/underwear.png` — 下着（ベース状態）
- `assets/costume/school.png` — スクール ※未差し替え（仮画像のまま）
- `assets/costume/nurse.png` — ナース
- `assets/costume/maid.png` — メイド
- `remove_bg.py` — 白背景を透過PNGに変換するスクリプト

## 方式
衣装ごとに「体・衣装・髪型が一枚絵に焼き込まれた完成イラスト」を丸ごと切り替える方式。
チップを選ぶと、対応する画像に差し替わるだけのシンプルな作り。
（髪型は絵に焼き込み済みのため、衣装とは独立に切り替えできません）

## 画像を追加・差し替えする手順

### 1. 背景を透過にする
Grokなどで生成した白背景の一枚絵を、透過PNGに変換します。

```
pip install pillow scikit-image scipy
python3 remove_bg.py 入力画像.jpg assets/costume/school.png
```

輪郭に白い縁が残る場合は第3引数で調整できます（デフォルト18）。

```
python3 remove_bg.py 入力画像.jpg assets/costume/school.png 10
```

### 2. 配置する
`assets/`以下の該当パスに、上のファイル名で保存するだけです。
既存の衣装（スクール／ナース／メイド／下着）を差し替える場合、コードの修正は不要です。

### 3. 衣装を新しく増やす場合
`app.js`の先頭の`costumes`配列に1行足します。

```js
{ id: "witch", label: "ウィッチ", src: "assets/costume/witch.png" }
```

## 画像を作る時の条件
- 正面向き・全身が収まる構図
- 白背景（透過処理しやすくするため）
- 衣装違いでもキャラクターの見た目（顔・髪・体型）を揃える
  ※Grokの編集機能で「衣装だけ変える」と一貫性を保ちやすい
