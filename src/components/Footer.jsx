import React from 'react'

const Footer = () => {
    return (
        <div className='bg-slate-800 text-white flex flex-col p-2 justify-center items-center  w-full'>
            <div className="logo font-bold text-white text-2xl">
                <span className='text-green-500'> &lt;</span>
                <span>TodoApp</span><span className='text-green-500'>&gt;</span>
            </div>
            <div className='flex justify-center items-center'> Manage Your Tasks Here </div>
        </div>
    )
}

export default Footer
