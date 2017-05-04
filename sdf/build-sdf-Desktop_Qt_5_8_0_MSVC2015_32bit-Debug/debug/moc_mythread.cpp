/****************************************************************************
** Meta object code from reading C++ file 'mythread.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.8.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../sdf/mythread.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mythread.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.8.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Mythread_t {
    QByteArrayData data[5];
    char stringdata0[23];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_Mythread_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_Mythread_t qt_meta_stringdata_Mythread = {
    {
QT_MOC_LITERAL(0, 0, 8), // "Mythread"
QT_MOC_LITERAL(1, 9, 3), // "err"
QT_MOC_LITERAL(2, 13, 0), // ""
QT_MOC_LITERAL(3, 14, 3), // "suc"
QT_MOC_LITERAL(4, 18, 4) // "succ"

    },
    "Mythread\0err\0\0suc\0succ"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Mythread[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x06 /* Public */,
       3,    1,   27,    2, 0x06 /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString,    1,
    QMetaType::Void, QMetaType::QString,    4,

       0        // eod
};

void Mythread::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Mythread *_t = static_cast<Mythread *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->err((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 1: _t->suc((*reinterpret_cast< QString(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (Mythread::*_t)(QString );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&Mythread::err)) {
                *result = 0;
                return;
            }
        }
        {
            typedef void (Mythread::*_t)(QString );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&Mythread::suc)) {
                *result = 1;
                return;
            }
        }
    }
}

const QMetaObject Mythread::staticMetaObject = {
    { &QThread::staticMetaObject, qt_meta_stringdata_Mythread.data,
      qt_meta_data_Mythread,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *Mythread::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Mythread::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_Mythread.stringdata0))
        return static_cast<void*>(const_cast< Mythread*>(this));
    return QThread::qt_metacast(_clname);
}

int Mythread::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QThread::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void Mythread::err(QString _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void Mythread::suc(QString _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
