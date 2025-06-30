import { Request,Response,NextFunction } from "express"
import { logger } from "../utils/logger"

export const reqHandler = (req:Request, res:Response, next:NextFunction)=>{
    logger.info({
        msg:"Reuest Incoming",
        method:req.method,
        url:req.url,
        body:req.body,
        timestamp: new Date().toISOString(),
    });

    next();
}