import base64

from ecies import decrypt

encrypted_vote_base64 = "BAc5u6ZIAPVHQ29STFyPfhR9OsFQ9UoXWrQACJ8FLglOsIiKRH8osLc9wBGWtnFwF2ZS3GVryndoHgHwgaz19v+MaXBBtnqa/Uav7y+Jl/SeKQdwiNXy+FSjI+ab6qgffdaElDCw1NextJe/xcbgJ5alNeevWj8oLFKLVLmRjpprtA7z/pZwQocfoZMYWu1Dy2XwDQc+U40/qCJccLbvjwUTsw=="
hashed_personal_number = "$argon2i$v=19$m=32768,t=16,p=2$NTY4NTQ0NTY4NTQ0$zIXD1GGgPTnriSudhry2LoXF8Le30pbJGUR7uWc0N70"

private_key = '0xd162e5a63826ab4d04b55afac3d6a265a986c4ad636d93d9d19ed95053fdfd92'
encrypted_vote = base64.b64decode(encrypted_vote_base64)
output = decrypt(private_key, encrypted_vote)
print(output)