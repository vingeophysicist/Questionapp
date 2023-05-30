import styled from "@emotion/styled";
import {AppBar, Toolbar, Typography} from "@mui/material";
import React from "react";
import MenuBookRoundedIcon from '@mui/icons-material/MenuBookRounded';


const StyledToolBar = styled(Toolbar)({
    display: "flex",
    justifyContent: "spaace-between"
})

const Navbar = ()=>{
    
    return (
        <AppBar position="stick">
            <StyledToolBar>
                <Typography variant="h6" sx={{ display: {xs:"none", sm: "block"} }}>LEARN SMARTLY</Typography>
                <MenuBookRoundedIcon></MenuBookRoundedIcon>
            </StyledToolBar>
        </AppBar>
    )
}


export default Navbar





