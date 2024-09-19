export const Hero1 = ({data}) => {
    return (
        <div>
            <section className="relative flex items-center justify-center h-screen bg-cover bg-center"
                     style={{backgroundImage: "url('/your-background-image.jpg')"}}>
                <div className="text-center text-white">
                    <h1 className="text-5xl font-bold mb-4">{data.heading}</h1>
                    <p className="text-xl mb-8">{data.subheading}</p>
                    <a href="#cta"
                       className="px-6 py-3 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors">
                        Get Started
                    </a>
                </div>
            </section>
        </div>
    )
}