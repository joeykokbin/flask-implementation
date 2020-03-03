# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet",
        id="uVwPO7GY8MY,tl1-Y6hXCt0,d4-qRim9LJQ,KYk_-w6r3lw,BOsikxHW0JQ,mAdX2PDeWnk,E4G5Y2ghqEQ,qy0aqjbwyVI,bJpgKoA8wrg,L3cJG44VPKU,8abxnqgZI7M,PH-GPARbRWs,9basY324N3U,NHL4ih5mXVA,arf04O7TV1A,JESaD6tqXiQ,4A3Hkdj59Do,5Pk1C9rWy68,xyp9hxLP67k,jY-8SrEGrLY,rMGy4-EBb8w,yj2j_K8c7XE,FsywAgJ42Ug,RoTrH4gHyaw,cJw5_zMEnps,PqW73EcFUKk,G1GJu8kd-ik,7q-VS6pyUiM,GXDJn3EEGOQ,OOiK7dNA_Vc,QruEsqdugkc,NzG4o-yeFMo,dMPTxTmZDzE,Th3cSnLluF0,F7VOCR3wWhM,QU-k9uGmhIQ,HY8HQUlepE0,uw4lBrezHLA,bHvgulGst4Y,SgiW_1Ry2dY,LtO_uWwTFog,3noLSXXni7M,Di4Vdn9e_G0,5yhX-FuqKao,Z7mqj5stFMg,SwWO5bA46jg,uyFOhoIWt78,hLsj8i3ihTo,DrzWGUGN6vY,SMIT1QZjk_M,3ZtN78fMk-g,BS1w-u8-C9Q,tSSMZj1BmKE,AipmQ2HWOxg,h7iUws89O0o,scVEgUdZFg0,FSUx5u_5q6Y,vcHtRxhe8rk,mQYdS3YCEss,S-m8ttdfQuw,ER81RCzEl7U,jIkISNw6TNo,USMWKNh3cB4,A3IF6doyeF0,XThLJZAmJUA,mpnshdmtE2Y,Mjz2aZ350vg,1n7t2ElxiBI,PNP3h2hmni4,piO-68zx2UQ,XNn3LLvZkrU,M-wat3TSQqY,Lx2kuVsWQwo,tBVlCSWH4Eo,2JYub2JxoDo,8DJXNQkitS4,aIZNHQC01K4,fxMhg22w34w,BB6ZCkvg39k,yxGczEE3NSw,hM_BYbi3vPI,Pa3ao2TVn1A,UTxt7WlPTuY,RVxEbCP8rhA,Np0LMwqtOVM,NSPgnoMBV4Q,fspYzg1Bmvg,i883yj99aBQ,vgX5M1eVhyw,luZEZgZNFAg,Sk5TFr-HOyE,sqyv-YIjQko,U3OvdvgMKs8,MghIH4J4My8,c4iupf23d9U,-ltu-ILo7rY,LlRl12drnls,0W9w-xUliS8,AULmGY1npqM,vCdeAHOtlzQ,bqy4XFraBlk,RdKwktG6-DA,msGOz8dbNB0,H_M_cU8cbYc,JO0u2hU4z6E,RQcYST8J5F8,ZdRq9EY7p0M,qw9oWC-r77A,nyRKk6K5l1w,KzqYzmtqQns,2BeQftjYNO4,eGZPnskG8DI,oka2orJZ_Og,GzEzNffkUhw,ZwAfROUJIPE,bWsAGMYXEYg,uM0nui4-Q3E,HTy5NxcKOx4,XjxDGssvfIg,xea94ZX65KY,vzIo6cSSi38,H_B0ZKVrJOE,u-q2dCtRlz0,f_iQUiCFuTA,gQZn7f4Y-tA,PjBu0Ipg6Wc,Cwa4kIYh58Q,C7Rs2I8WtDw,1gYA0UVEAFA,NxYQZj_FBaI,8MD7IECmfyY,uPKj_6-ZezQ,sUZbfaYyL-s,QvtQI4tq_XU,17lp_x27_RI,pH2tu8nD1Ic,tPdi0cUPg0Q,v6HbZrUqyIQ,huCLAMbo8uo,o2XpKKAx5yo,uXAuzS8V9AY,R5bYP2NlAf4,K5TeFK5-xjU,HgmSm67tZZ8,u_EcIsot0Vg,0cWAPfKyrSA,JRhSBAZNmtM,b2O3x5xK3Fg,aCUC5GVX1VI,fv-mwCCBqAs,aQaf3gzXxig,3-9iKEBukaQ,6HDc8B1RxzU,VF6WPDZF9kk,aC1gX08CM9M,ex3hbXchxiQ,RApzagDfqdc,qBGepey5_o4,nq9x9GtUuu4,1kC51RAGef4,jrLJ4ra7s3E,1nVKV3LyCQA,8aP8sbQuQDg,IYOa54hxulQ,dVm8GzbW-fA,5Ts9aGTzAV8,TRhCHSaG_58"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
