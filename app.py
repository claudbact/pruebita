from flask import Flask,request ,render_template



APP=Flask(__name__,
    static_folder='static',
    # static_url_path='/public'
    static_url_path='/',
    template_folder='templates',

)

@APP.route('/')

def home():
    return 'Hola mundo'

#VISTAS
@APP.route('/home')
def home_view():
    #return render_template('demo.html'), 200
    locals = {
        'nombre': 'Pepe',
        'edad': 32,
        'title': 'Home 1',
        'bicicletas': [
            {
                'img': 'cici01',
                'alt': 'K036',
            },
            {
                'img': 'cici02',
                'alt': 'Tempo01',
            },
             {
                'img': 'cici02',
                'alt': 'Tempo01',
            },
        ],
    }
    return render_template(
        'demo.html', 
        locals=locals,
    ), 200
@APP.route('/home2')
def home_view2():
    locals = {
        'mascota': 'Sila',
    }
    return render_template(
        'demo2.html', 
        locals=locals,
    ), 200

@APP.route('/demo')

def demo():
    return 'Hola demo'

@APP.route('/demo_path/<name>/<int:age>',methods=['GET','POST'])

def demo_path(name,age):
   
    
    return 'path parameter -> nombre : %s, edad : %d' % (name, age),200
    
@APP.route('/demo_query',methods=['GET','POST'])

def demo_query():
   
    name=request.args.get('name')
    age=int (request.args.get('age'))
    return 'path parameter -> nombre : %s, edad : %d' % (name, age),200
       
@APP.route('/demo_post', methods=['POST'])
def demo_post():
    name = request.form['name']
    age = int(request.form['age'])
    #print(request.method)
    #print('post parameter -> nombre : %s, edad : %d' % (name, age))
    return 'post parameter -> nombre : %s, edad : %d' % (name, age),200

if __name__ == '__main__':
    APP.run(
        debug=True,
        port=9911
    )