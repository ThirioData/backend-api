import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { Container, Menu, Header } from 'semantic-ui-react'
import { Link } from 'react-router-dom'
import Routes from './Routes'
import RouteNavItem from './containers/RouteNavItem'

class App extends Component {
  render() {
    return (
      <Container className="App">
        <Menu className="navigation">
          <Menu.Item name="Thirio" className="navigationTitle" position="left" href="/">
            <Header as="h1">Thirio</Header>
          </Menu.Item>
          <RouteNavItem href="/signup">Signup</RouteNavItem>
          <RouteNavItem href="/login">Login</RouteNavItem>
        </Menu>
        <Routes />
      </Container>
    );
  }
}

export default App;
