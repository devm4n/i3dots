import { createContext } from "react";

export const CommentContext = createContext()

export const CommnetProvider = ({children}) =>{
    return(
        <CommentContext.Provider>
            {children}
        </CommentContext.Provider>
    )
}