import React from 'react';

const PageHeader = () => {
  return (
    <header style={headerStyle}>
      <h1>Bem-vindo à página</h1>
      <nav>
        <ul style={navListStyle}>
          <li><a href="#home">Início</a></li>
          <li><a href="#about">Sobre</a></li>
          <li><a href="#contact">Contato</a></li>
        </ul>
      </nav>
    </header>
  );
};

const headerStyle = {
  margin: 0,
  backgroundColor: '#4CAF50',
  color: 'white',
  padding: '20px',
  textAlign: 'center'
};

const navListStyle = {
  listStyleType: 'none',
  padding: 0,
  marginTop: '10px',
};

export default PageHeader;