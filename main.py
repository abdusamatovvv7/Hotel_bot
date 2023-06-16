import logging

from aiogram import Bot, Dispatcher, executor, types
from tugmalar import *

API_TOKEN = ''


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'hotel'])
async def send_welcome(message: types.Message):
    await message.reply("Salom bu Hotel🏨 bot✅\n \nAdmin: @muhammadaminuz7.", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Joy band qilish ✅")
async def send_welcome(message: types.Message):
    await message.reply("Joy band qilindi ✅")
######################################################
# YUNUSOBOD TUMANI
@dp.message_handler(text="Yunusobod")
async def echo(message: types.Message):
    await message.answer("Yunusoboddagi hotellar", reply_markup=yunusobod_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Radisson")
async def echo(message: types.Message):
    await message.answer("Radisson haqida")
    await message.answer_photo("https://sitara.com/upload/resize_cache/iblock/64b/1000_1000_1/radisson.jpg",
                               caption="Kuniga = 100$", reply_markup=radisson_narxi_inline)                          
    await message.answer_location(41.33491049206537, 69.28498610928187)



@dp.message_handler(text="Khan Orda Hotel")
async def echo(message: types.Message):
    await message.answer("Khan Orda Hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/322358545.jpg?k=aa4e26352683a947ffd018972f0c872d8bee0834bd91b4b301399414b5575347&o=&hp=1",
                               caption="Kuniga = 868.000 UZS", reply_markup=khan_narxi_inline)
    await message.answer_location(41.37007859272387, 69.28572336695501)   


# @dp.callback_query_handler(text="Khan")
# async def echo(call: types.CallbackQuery):
#     await call.message.answer("Khan Orda Hotel haqida")

#################################################################
#CHILONZOR
@dp.message_handler(text="Chilonzor")
async def echo(message: types.Message):
    await message.answer("Chilonzordagi hotellar", reply_markup=chilonzor_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Rohat hotel")
async def echo(message: types.Message):
    await message.answer("Rohat hotel haqida")
    await message.answer_photo("https://www.booking.com/hotel/uz/rohat.ru.html?aid=356938&label=metagha-link-LUUZ-hotel-1084490_dev-desktop_los-1_bw-15_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-17481824557_mcid-10_ppa-1_clrid-0_ad-1_gstkid-0_checkin-20230627_&sid=c80bcbedb5462f1cb92d2a867c9a45ed&all_sr_blocks=108449002_190363471_0_1_0;checkin=2023-06-27;checkout=2023-06-28;dest_id=-2579372;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=108449002_190363471_0_1_0;hpos=1;matching_block_id=108449002_190363471_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=108449002_190363471_0_1_0__7300;srepoch=1686572709;srpvid=8a405752bc920137;type=total;ucfs=1&#",
                               caption="Kuniga = 835.000 UZS", reply_markup=Rohat_narxi_inline)
    await message.answer_location(41.28214017760285, 69.21950198072666)   
@dp.message_handler(text="Qushbegi Plaza Hotel")
async def echo(message: types.Message):
    await message.answer("Qushbegi Plaza Hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/300796045.jpg?k=0da96fa440abe55f671495d441a1f1bc0c0fa5bc8e2666a773fb8c49418998c0&o=&hp=1  ",
                               caption="Kuniga = 1.486.000 UZS", reply_markup=Qushbegi_narxi_inline)
    await message.answer_location(41.272592779441815, 69.2451719957851)   


# #################################################################
# #
# @dp.message_handler(text="")
# async def echo(message: types.Message):
#     await message.answer("dagi hotellar", reply_markup=_hotels_keyboard)

# @dp.message_handler(text="⬅️ Ortga")
# async def echo(message: types.Message):
#     await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

# @dp.message_handler(text="")
# async def echo(message: types.Message):
#     await message.answer(" haqida")
#     await message.answer_photo("",
#                                caption="Kuniga =  UZS", reply_markup=)

# @dp.message_handler(text="")
# async def echo(message: types.Message):
#     await message.answer(" haqida")
#     await message.answer_photo("",
#                                caption="Kuniga =  UZS", reply_markup=)                               


#################################################################
#BEKTEMIR
@dp.message_handler(text="Bektemir")
async def echo(message: types.Message):
    await message.answer("Bektemirdagi hotellar", reply_markup=bektemir_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Ada hotel")
async def echo(message: types.Message):
    await message.answer("Ada hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5HTkDhqMQP8LRNMgzWOKoKhcfVU18tCF4gbljRs0rRt0YP-AyGm7fypW1BT6tyZMXdPg9QgsBCYxSfPKaRCCznSnjPWRe-YM_er26zEDoJ8UYFOpjT5N2S1NUrVdsQDmVbTCt-OcJMaCreGLdwAQx_Nt-JsPEpVsvJilAW3PFO5CMJ8N63Gh84j=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga =  643.000 UZS", reply_markup=ada_narxi_inline)
    await message.answer_location(41.244279747151815, 69.29362366694784) 

@dp.message_handler(text="Ayva hotel")
async def echo(message: types.Message):
    await message.answer("Ayva hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipPuj3QOBNcf9De4nXaIn98mXQthADIuc1Uvxq9r=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga =  470.000 UZS", reply_markup=ayva_narxi_inline) 
    await message.answer_location(41.24401188075278, 69.30675752276998)   


#################################################################
#MIROBOD
@dp.message_handler(text="Mirobod")
async def echo(message: types.Message):
    await message.answer("Miroboddagi hotellar", reply_markup=mirobod_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Grand Mir")
async def echo(message: types.Message):
    await message.answer("Grand Mirrand haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/171720699.jpg?k=de52de5c89e7653b2db0eb440143e7b319f0574c484f3e30e2f0136c3a0f5d86&o=&hp=1",
                               caption="Kuniga = 1.545.000 UZS", reply_markup=Grand_narxi_inline)
    await message.answer_location(41.296570305054225, 69.26784362277306)   
@dp.message_handler(text="Shodlik Palace")
async def echo(message: types.Message):
    await message.answer("Shodlik Palace haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/59076703.jpg?k=85c56b9c3bf581dd450455e0cc5ff5fa4b1c0bec616889fb24a5abc4faa75f73&o=&hp=1",
                               caption="Kuniga = 767.000 UZS", reply_markup=shodlik_narxi_inline) 
    await message.answer_location(41.318162120240245, 69.26113109024094)    


#################################################################
#MIRZO ULUG'BEK
@dp.message_handler(text="Mirzo Ulug'bek")
async def echo(message: types.Message):
    await message.answer("Mirzo Ulug'bekdagi hotellar", reply_markup=mirzoo_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Mirzo hotel")
async def echo(message: types.Message):
    await message.answer("Mirzo hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/196099136.jpg?k=87713a5d90992f966ae7c3a24e493be7e9b73a5b0f31be7419ae2b48535fca86&o=&hp=1",
                               caption="Kuniga = 1.029.000 UZS", reply_markup=Mirzo_narxi_inline)
    await message.answer_location(41.3244262721051, 69.24175436695243)   
@dp.message_handler(text="Sarbon hotel")
async def echo(message: types.Message):
    await message.answer("Sarbon hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/219401978.jpg?k=0560252055a135d60e50782339ef01cf19691de1501b073d4b3970985e41cf86&o=&hp=1",
                               caption="Kuniga = 880.000 UZS", reply_markup=sarbon_narxi_inline) 
    await message.answer_location(41.335906153836326, 69.29207240928197)   


#################################################################
#OLMAZOR
@dp.message_handler(text="Olmazor")
async def echo(message: types.Message):
    await message.answer("Olmazordagi hotellar", reply_markup=olmazor_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Hotel avesto")
async def echo(message: types.Message):
    await message.answer("Hotel Avesto haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipMD3ZZFpyDZ-EYoMLT_bzL_wh5L3ELunrWp2MdI=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 400.000 UZS", reply_markup=avesto_narxi_inline)
    await message.answer_location(41.34033523078731, 69.21686089578893)

@dp.message_handler(text="Jules Verne")
async def echo(message: types.Message):
    await message.answer("Jules Verne haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/366810495.jpg?k=eb3a45da1a90978d25899293b7522691c478cbc15026b98e83f0929d0aefe572&o=&hp=1",
                               caption="Kuniga = 252.000 UZS", reply_markup=jules_narxi_inline) 
    await message.answer_location(41.33694458431629, 69.27213481254081)   

#################################################################
#SERGELI
@dp.message_handler(text="Sergeli")
async def echo(message: types.Message):
    await message.answer("Sergelidagi hotellar", reply_markup=Sergeli_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="South Hotel")
async def echo(message: types.Message):
    await message.answer("South Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipMKQzV2E10PihU8xlfLI2rBK79cFj8M_aH-PX7R=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 609.000 UZS", reply_markup=south_narxi_inline)
    await message.answer_location(41.25804414055297, 69.22772099763306)

@dp.message_handler(text="Atlantis Hotel")
async def echo(message: types.Message):
    await message.answer("Atlantis Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipPaalg2HfVHzNj6HDJa4vEUVOedznjuTvlhtNfk=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 861.000 UZS", reply_markup=atlantis_narxi_inline) 
    await message.answer_location(41.216197041172975, 69.21959099393291)   


#################################################################
#Shayxontoxur
@dp.message_handler(text="Shayxontoxur")
async def echo(message: types.Message):
    await message.answer("Shayxontoxurdagi hotellar", reply_markup=Shayxontoxur_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Lotte City Hotel Tashkent Palace")
async def echo(message: types.Message):
    await message.answer("Lotte City Hotel Tashkent Palace haqida")
    await message.answer_photo("https://www.booking.com/hotel/uz/tashkent-palace-hotel.ru.html?aid=356938&label=metagha-link-LUUZ-hotel-347792_dev-desktop_los-1_bw-4_dow-Saturday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-17481824557_mcid-10_ppa-1_clrid-0_ad-1_gstkid-0_checkin-20230617_&sid=888b32833e80c6386671cd61cd913e14&all_sr_blocks=34779211_179802167_0_1_0;checkin=2023-06-17;checkout=2023-06-18;dest_id=-2579372;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=34779211_179802167_0_1_0;hpos=1;matching_block_id=34779211_179802167_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=34779211_179802167_0_1_0__17500;srepoch=1686676514;srpvid=6f6c7950932702c7;type=total;ucfs=1&#",
                               caption="Kuniga = 2.008.000 UZS", reply_markup=lotte_narxi_inline)
    await message.answer_location(41.30986676889816, 69.2685829669516)
       
@dp.message_handler(text="The Royal Mezbon Hotel & SPA")
async def echo(message: types.Message):
    await message.answer("The Royal Mezbon Hotel & SPA haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/208881579.jpg?k=648a0b78a63fdcb13e87b534a576cdf50fba9fcfeac22bdc9ad91360b85768e7&o=&hp=1",
                               caption="Kuniga = 1.043.000 UZS", reply_markup=the_narxi_inline)  
    await message.answer_location(41.26582671748547, 69.24401794975796)   


#################################################################
#YAKKASAROY
@dp.message_handler(text="Yakkasaroy")
async def echo(message: types.Message):
    await message.answer("Yakkasaroydagi hotellar", reply_markup=Yakkasaroy_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Gabrielle International Hotel")
async def echo(message: types.Message):
    await message.answer("Gabrielle International Hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/262039775.jpg?k=23fdb6b2c7930d51ad0fdd7862a287a35e70c7802e55dda66ef225f528852401&o=&hp=1",
                               caption="Kuniga = 1.216.000 UZS", reply_markup=Gabrielle_narxi_inline)
    await message.answer_location(41.288048443161436, 69.25761173811479)

@dp.message_handler(text="Grand Mir Hotel")
async def echo(message: types.Message):
    await message.answer("Grand Mir Hotel haqida")
    await message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/172603655.jpg?k=be26b08d1e117fb6bb69ebd7125f1bf2ee156fa9cfa39a398eac7bea9479ef6f&o=&hp=1",
                               caption="Kuniga = 85$ UZS", reply_markup=grandmir_narxi_inline)
    await message.answer_location(41.2965622444403, 69.26789726695084)   

#################################################################
#UCHTEPA
@dp.message_handler(text="Uchtepa")
async def echo(message: types.Message):
    await message.answer("Uchtepadagi hotellar", reply_markup=Uchtepa_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Vatan Plaza Hotel")
async def echo(message: types.Message):
    await message.answer("Vatan Plaza Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipNWpNBRAOrXsPu_IJfeyFdyAub_sZLy1qMXhB-G=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 602.000 UZS", reply_markup=vatan_narxi_inline)
    await message.answer_location(41.27944098886753, 69.17662742277203)   

@dp.message_handler(text="Aurora Hotel")
async def echo(message: types.Message):
    await message.answer("Aurora Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/gps-proxy/AE4_-5HkdyWsf6PoW7oniJMJ0hj1VuZXxf9mhxkJoAVmoOeElq6gvHgqxyuq70WzAGc_tbPUE4rHdrTTgu60x7ezM6wF9625x09kHwTcGrZCkT_QNV3wMrrai3CdVwO9DNtO2KkQXCqxZ6-qClQrcFCedDDmHYOY7EoFJXJ7zdC-mDRXfthlVtyDOwCR4g=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 551.000 UZS", reply_markup=aura_narxi_inline)  
    await message.answer_location(41.27785355593326, 69.1761640939364)   

#################################################################
#YANGIHAYOT
@dp.message_handler(text="Yangihayot")
async def echo(message: types.Message):
    await message.answer("Yangihayotdagi hotellar", reply_markup=Yangihayot_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Garnet Hotel")
async def echo(message: types.Message):
    await message.answer("Garnet Hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipOkc1Mb09ZXhCCEiXdM6xNMo9JwqolixQVTf1Oh=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 875.000 UZS", reply_markup=garnet_narxi_inline)
    await message.answer_location(41.293464358623936, 69.26741510357813)  

@dp.message_handler(text="Simma Hotel")
async def echo(message: types.Message):
    await message.answer("Simma Hotel haqida")
    await message.answer_photo("https://images.trvl-media.com/lodging/40000000/39430000/39423400/39423374/9479aab4.jpg?impolicy=resizecrop&rw=1200&ra=fit",
                               caption="Kuniga = 101$ UZS", reply_markup=simma_narxi_inline) 
    await message.answer_location(41.22366445495267, 69.1994153939333)   
#################################################################
#YASHNOBOD
@dp.message_handler(text="Yashnobod")
async def echo(message: types.Message):
    await message.answer("Yashnoboddagi hotellar", reply_markup=Yashnobod_hotels_keyboard)

@dp.message_handler(text="⬅️ Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=rayonlar_keyboards)

@dp.message_handler(text="Harmony Hotel")
async def echo(message: types.Message):
    await message.answer("Harmony Hotel haqida")
    await message.answer_photo("https://lh5.googleusercontent.com/p/AF1QipOA7spxJLl6J_T5p7KroQ_6__xQavxOmNPs__-u=w253-h189-k-no",
                               caption="Kuniga = 664.000 UZS", reply_markup=harmony_narxi_inline)
    await message.answer_location(41.26888269850048, 69.31400295399003)

@dp.message_handler(text="Davan hotel")
async def echo(message: types.Message):
    await message.answer("Davan hotel haqida")
    await message.answer_photo("https://lh3.googleusercontent.com/p/AF1QipOicq03ruizqbhjEnREy6WLEyf6kOYCrYoCz5Ta=w296-h202-n-k-rw-no-v1",
                               caption="Kuniga = 457.000 UZS", reply_markup=davon_narxi_inline)   
    await message.answer_location(41.25885002494187, 69.3195209526938)   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)