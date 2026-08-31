document.addEventListener("DOMContentLoaded", function () {
  const justGenerated = document.body.dataset.justGenerated === "true";

  if (justGenerated) {
    fireConfetti();
  }

  const downloadPngBtn = document.getElementById("download-png-btn");
  const downloadPdfBtn = document.getElementById("download-pdf-btn");
  const printBtn = document.getElementById("print-btn");

  if (downloadPngBtn) downloadPngBtn.addEventListener("click", downloadAsPng);
  if (downloadPdfBtn) downloadPdfBtn.addEventListener("click", downloadAsPdf);
  if (printBtn) printBtn.addEventListener("click", () => window.print());
});

function fireConfetti() {
  const canvas = document.getElementById("confetti-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener("resize", resize);

  const colors = ["#c9a24b", "#1c3d5a", "#a97e2b", "#e9e5da", "#7a6a3e"];
  const pieces = Array.from({ length: 140 }, () => ({
    x: Math.random() * canvas.width,
    y: -20 - Math.random() * canvas.height * 0.5,
    size: 5 + Math.random() * 6,
    color: colors[Math.floor(Math.random() * colors.length)],
    speedY: 2 + Math.random() * 3,
    speedX: -1.5 + Math.random() * 3,
    rotation: Math.random() * 360,
    rotationSpeed: -6 + Math.random() * 12,
  }));

  let frame = 0;
  const maxFrames = 220;

  function draw() {
    frame++;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    pieces.forEach((p) => {
      p.x += p.speedX;
      p.y += p.speedY;
      p.rotation += p.rotationSpeed;

      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rotation * Math.PI) / 180);
      ctx.fillStyle = p.color;
      ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
      ctx.restore();
    });

    if (frame < maxFrames) {
      requestAnimationFrame(draw);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  requestAnimationFrame(draw);
}

function downloadAsPng() {
  const target = document.getElementById("certificate-capture-area");
  if (typeof html2canvas === "undefined") {
    window.print();
    return;
  }
  html2canvas(target, { scale: 2, backgroundColor: "#fffdf8" }).then((canvas) => {
    const link = document.createElement("a");
    link.download = (document.body.dataset.certificateId || "certificate") + ".png";
    link.href = canvas.toDataURL("image/png");
    link.click();
  });
}

function downloadAsPdf() {
  const target = document.getElementById("certificate-capture-area");
  if (typeof html2canvas === "undefined" || typeof window.jspdf === "undefined") {
    window.print();
    return;
  }
  html2canvas(target, { scale: 2, backgroundColor: "#fffdf8" }).then((canvas) => {
    const { jsPDF } = window.jspdf;
    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF({
      orientation: "landscape",
      unit: "px",
      format: [canvas.width, canvas.height],
    });
    pdf.addImage(imgData, "PNG", 0, 0, canvas.width, canvas.height);
    pdf.save((document.body.dataset.certificateId || "certificate") + ".pdf");
  });
}