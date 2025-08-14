import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { 
  Container, 
  AppBar, 
  Toolbar, 
  Typography, 
  Button, 
  Box,
  Avatar,
  Menu,
  MenuItem,
  IconButton
} from '@mui/material';
import { 
  AutoAwesome, 
  AccountCircle,
  Logout,
  GitHub
} from '@mui/icons-material';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import HomePage from './pages/HomePage';
import CallbackPage from './pages/CallbackPage';
import Dashboard from './components/Dashboard';

const AppHeader: React.FC = () => {
  const { user, logout } = useAuth();
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);

  const handleMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    logout();
    handleClose();
  };

  return (
    <AppBar position="static" elevation={1}>
      <Toolbar>
        <AutoAwesome sx={{ mr: 2 }} />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Test Case Generator
        </Typography>
        
        {user && (
          <Box display="flex" alignItems="center" gap={1}>
            <Typography variant="body2" sx={{ mr: 1 }}>
              {user.name || user.login}
            </Typography>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleMenu}
              color="inherit"
            >
              <Avatar 
                src={user.avatar_url} 
                alt={user.login}
                sx={{ width: 32, height: 32 }}
              />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorEl}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorEl)}
              onClose={handleClose}
            >
              <MenuItem onClick={() => window.open(user.html_url, '_blank')}>
                <GitHub sx={{ mr: 1 }} />
                View GitHub Profile
              </MenuItem>
              <MenuItem onClick={handleLogout}>
                <Logout sx={{ mr: 1 }} />
                Sign Out
              </MenuItem>
            </Menu>
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <AppHeader />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/callback" element={<CallbackPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;