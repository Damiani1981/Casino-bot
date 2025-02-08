import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.ext import Application

application = Application.builder().token("7873205367:AAGa_U3emXoVSnlafRrFhCA4l0Qc7nMNTx8").build()
# Aplicamos nest_asyncio para evitar errores en Google Colab o entornos con bucles activos
nest_asyncio.apply()

# Token del bot (reemplazar con el real)
TOKEN = "7873205367:AAGa_U3emXoVSnlafRrFhCA4l0Qc7nMNTx8"

# 📌 Funciones de los comandos del bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🎰 ¡Bienvenido a FichinBot! Presiona el menú para conocer más.")

async def promos(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🎁 ¡Aprovechá nuestras promociones!\n"
                                    "💥 Recomendanos y llevate un 20% extra en fichas por cada referido\n"
                                    "📌 Válido con cargas de $1.000 a $5.000\n"
                                    "📲 No te quedes afuera, sumá fichas YA.\n"
                                    "💣 Cuantos más referidos, más ganás… ¡Aprovechá esta promo antes de que termine! 🚀🏆")

async def juegos(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🎰 **Juegos Disponibles**\n\n"
                                    "🔹 **Tragamonedas**, **Ruleta**, **Póker**, **Blackjack** y más 🎲♠️\n"
                                    "💻 **Proveedores:** Pragmatic Play, MicroGaming, Ruby Play y más.\n"
                                    "📌 Para ver plataformas, usá /plataformas.")

async def ayuda(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("ℹ️ **¿Necesitas ayuda?**\n\n"
                                    "👉 **Administración:** /administracion\n"
                                    "👉 **Plataformas disponibles:** /plataformas\n"
                                    "👉 **Juegos disponibles:** /juegos\n"
                                    "Si tenés dudas, preguntame. ¡Estoy para ayudarte! 🎰✨")

async def plataformas(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🌐 **Plataformas Disponibles**\n\n"
                                    "👑 jugavip.net\n🏡 ganaen.casa\n📱 Celua-puestas.com\n"
                                    "😎 bet30.vip\n⚡ Casino-zeus.bet\n🐯 Magiplay.vip\n\n"
                                    "📌 **Elegí tu plataforma favorita y pedí un usuario a un cajero.**")

async def quiero_usuario(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🆕 **¿Querés crear un usuario?**\n\n"
                                    "📍 **Aquí te dejo el contacto con los cajeros de nuestra red**.\n"
                                    "📲 [Unirte al Canal de Cajeros](https://whatsapp.com/channel/0029VaG0xEe2kNFkRdD9eK08)\n\n"
                                    "⚠️ **Cada cajero tiene su propio horario de atención. Consultá su disponibilidad.**")

async def administracion(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("📢 **Contacto de la Administración**\n"
                                    "👤 **Encargada:** María Laura Damiani\n"
                                    "📩 **WhatsApp Directo:** [Contactar](https://wa.me//3487657442)\n"
                                    "📌 **Para dudas o información sobre el casino, contactanos.** 🎰✨")

async def canal(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("📢 **Canal Oficial**\n"
                                    "🔗 [Unirte al canal](https://whatsapp.com/channel/0029VaG0xEe2kNFkRdD9eK08)")

async def cajeros(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🏧 **Cajeros Oficiales**\n"
                                    "📍 **Lista de cajeros en nuestro canal:**\n"
                                    "🔗 [Ver cajeros oficiales](https://whatsapp.com/channel/0029VaG0xEe2kNFkRdD9eK08)\n\n"
                                    "📌 **Recargá con confianza y jugá sin preocupaciones!** 🎰🔥")
async def cajeros(update: Update, context: CallbackContext):
    mensaje = (
        "🏧 *Lista de Cajeros Oficiales:* \n\n"
        "📌 *Elige a tu cajero y presiona su nombre para acceder a su WhatsApp directo:* \n\n"
    )
    cajeros = {
        "LAURA DAMIANI": "https://wa.me/+543487657442",
        "LUANA": "https://wa.me/+5493445431634",
        "FELIPE": "https://wa.me/+5493743590513",
        "MARCELA": "https://wa.me/+5493445402579",
        "BACHI": "https://wa.me/+543487547291",
        "PABLO": "https://wa.me/+5491127123785",
        "YAMILA": "https://wa.me/+5493487206698",
        "IARA": "https://wa.me/+5493487729959",
        "LORE": "https://wa.me/+5493487623785",
        "PAULA": "https://wa.me/+5493445537129",
        "FLOR": "https://wa.me/+5493487689059",
        "COCO": "https://wa.me/+5493445470475",
        "ABI": "https://wa.me/+5493534090874",
        "CELI": "https://wa.me/543487200962",
        "DAIANA": "https://wa.me/3487212168",
        "DAI MILLAN": "https://wa.me/1140363509",
        "JOSEFINA": "https://wa.me/3487511198",
        "CELE": "https://wa.me/3487719457",
        "MARIANELA": "https://wa.me/3487226376",
        "GABI": "https://wa.me/3445475600",
        "KAREN ARGUELLO": "https://wa.me/+5493445401998",
        "LOLO": "https://wa.me/3487537149",
        "JOA": "https://wa.me/+5493487585866",
    }
    
    for nombre, enlace in cajeros.items():
        mensaje += f"📌 [{nombre}]({enlace})\n"

    await update.message.reply_text(mensaje, parse_mode="Markdown", disable_web_page_preview=True)

async def buscar_cajero(update: Update, context: CallbackContext):
    nombre_buscado = update.message.text.strip().upper()  # Convierte el nombre en mayúsculas para evitar errores
    cajeros = {
        "LAURADAMIANI": "+543487657442",
        "LUANA": "+5493445431634",
        "FELIPE": "+5493743590513",
        "MARCELA": "+5493445402579",
        "CAJERO BACHI": "+543487547291",
        "CAJERO PABLO": "+5491127123785",
        "CAJERA YAMILA": "+5493487206698",
        "CAJERA IARA": "+5493487729959",
        "CAJERA LORE": "+5493487623785",
        "CAJERA PAULA": "+5493445537129",
        "CAJERA FLOR": "+5493487689059",
        "CAJERO COCO": "+5493445470475",
        "CAJERA ABI": "+5493534090874",
        "CAJERA CELI": "+543487200962",
        "CAJERA DAIANA": "+3487212168",
        "CAJERA DAI MILLAN": "+1140363509",
        "CAJERA JOSEFINA": "+3487511198",
        "CAJERA CELE": "+3487719457",
        "CAJERA MARIANELA": "+3487226376",
        "CAJERA GABI": "+3445475600",
        "CAJERA KAREN ARGUELLO": "+5493445401998",
        "CAJERA LOLO": "+3487537149",
        "CAJERA JOA": "+5493487585866",
    }

    if nombre_buscado in cajeros:
        numero = cajeros[nombre_buscado]
        mensaje = f"📌 *{nombre_buscado}* - WhatsApp: [{numero}](https://wa.me/{numero})"
    else:
        mensaje = "⚠️ No encontré ese cajero en la lista. Verifica el nombre y vuelve a intentarlo."

    await update.message.reply_text(mensaje, parse_mode="Markdown", disable_web_page_preview=True)
# 📌 Respuestas automáticas personalizadas
async def responder_mensaje(update: Update, context: CallbackContext) -> None:
    nombre_usuario = update.message.from_user.first_name
    texto_usuario = update.message.text.lower()

    respuestas = {
        "hola": f"👋 ¡Hola {nombre_usuario}! Soy *Fichíta*, el bot de *Red ML*. 🎰 ¿En qué puedo ayudarte,puedes ir a menu, o poner quiero jugar?",
        "quiero jugar": f"🎰 ¡Sí, cómo no, {nombre_usuario}! Acá te dejo opciones:\n\n"
                        "📌 **Quiero un usuario** → /quierousuario\n"
                        "📌 **Cajeros disponibles** → /cajeros\n"
                        "📌 **Plataformas de juego** → /plataformas\n\n"
                        "🔥 **Elegí una opción y comenzá a jugar. ¡Mucha suerte!** 🎲",
    }

    respuesta = respuestas.get(texto_usuario, f"No entiendo esa pregunta, {nombre_usuario}. Usa /ayuda.")
    await update.message.reply_text(respuesta)

# 📌 Configuración del bot
async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("promos", promos))
    application.add_handler(CommandHandler("juegos", juegos))
    application.add_handler(CommandHandler("ayuda", ayuda))
    application.add_handler(CommandHandler("plataformas", plataformas))
    application.add_handler(CommandHandler("quierousuario", quiero_usuario))
    application.add_handler(CommandHandler("administracion", administracion))
    application.add_handler(CommandHandler("canal", canal))
    application.add_handler(CommandHandler("cajeros", cajeros))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensaje))

    import asyncio

if __name__ == "__main__":
    print("🤖 Bot en ejecución...")
    asyncio.run(application.run_polling())


