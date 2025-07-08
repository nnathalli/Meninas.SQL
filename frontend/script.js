  document.getElementById('integranteForm').addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(this);
      const data = Object.fromEntries(formData.entries());
      fetch('/api/integrante', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
          alert(data.message);
      })
      .catch((error) => {
          console.error('Erro:', error);
      });
  });
