window.addEventListener('load', () => {
  const chatBox = document.getElementById('chat-box');

  // チャットボックスのスクロールを一番下に設定
  chatBox.scrollTop = chatBox.scrollHeight;

  // Ctrl + Enter でフォームを送信
  const form = document.getElementById('chat-form');
  const textarea = document.getElementById('user-input');

  textarea.addEventListener('keydown', (event) => {
    // Ctrl + Enter
    if (
      !event.altKey &&
      !event.metaKey &&
      !event.shiftKey &&
      event.ctrlKey &&
      event.key === 'Enter'
    ) {
      event.preventDefault();
      form.submit();
    }
  });
});
