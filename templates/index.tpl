<!--ここでbase.tplを利用することを宣言-->
% rebase('templates/base.tpl')
<div>
  <h3>あなたが捕まえたアワビの特徴は？</h3>
</div>
<form action="/abalone" method="post">
  <fieldset>
    <legend align="left">入力フォーム</legend>
    <!--送信ボタン-->
    <div class="input-group">
      <input type="submit" class="primary" value="年齢を当てる">
    </div>
  </fieldset>
</form>
