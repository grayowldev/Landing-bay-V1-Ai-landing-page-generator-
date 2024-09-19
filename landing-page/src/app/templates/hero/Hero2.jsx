export const Hero2 = ({data}) => {
    return (
        <div>
            <section
                className="flex flex-col-reverse md:flex-row items-center justify-between h-screen p-8 #EAE9E5" style={{background: '#EAE9E5'}}>
                <div className="md:w-1/2 text-center md:text-left">
                    <h1 className="text-5xl font-bold mb-4">{data.heading}</h1>
                    <p className="text-xl mb-8">{data.subheading}</p>
                    <a href="#cta"
                       className="inline-block px-6 py-3 bg-orange-500 text-white rounded-md hover:bg-orange-600 transition-colors">
                        Get Started
                    </a>
                </div>
                <div className="md:w-1/2">
                    <img
                        src="https://images.pexels.com/photos/2325447/pexels-photo-2325447.jpeg"
                        alt="Hero Image"
                        className="w-full h-auto object-cover rounded-lg shadow-lg"
                    />
                </div>
            </section>
        </div>
    )
}