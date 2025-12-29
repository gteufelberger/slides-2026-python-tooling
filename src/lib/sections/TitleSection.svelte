<script>
  import qrCode from "$lib/assets/qr-code-link.png";
</script>

<section>
  <h1>Python Tooling in 2026</h1>
  <p>
    What's new? What's good?
    <br />
    Tips and tricks
  </p>

  <div class="qr-section">
    <span>Link to slides:</span>
    <img src={qrCode} alt="QR code link to slides" class="qr-code" />
  </div>
</section>

<style>
  .qr-section {
    display: flex;
    align-items: center;
    gap: 1rem;
    justify-content: center;
  }

  .qr-code {
    width: 150px;
    height: 150px;
  }
</style>
