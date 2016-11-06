/****************************************************************************
** Meta object code from reading C++ file 'rosinterface.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.2.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../include/rosinterface/rosinterface.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'rosinterface.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.2.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_ROSInterfaceBase_t {
    QByteArrayData data[1];
    char stringdata[18];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    offsetof(qt_meta_stringdata_ROSInterfaceBase_t, stringdata) + ofs \
        - idx * sizeof(QByteArrayData) \
    )
static const qt_meta_stringdata_ROSInterfaceBase_t qt_meta_stringdata_ROSInterfaceBase = {
    {
QT_MOC_LITERAL(0, 0, 16)
    },
    "ROSInterfaceBase\0"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_ROSInterfaceBase[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

void ROSInterfaceBase::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObject ROSInterfaceBase::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_ROSInterfaceBase.data,
      qt_meta_data_ROSInterfaceBase,  qt_static_metacall, 0, 0}
};


const QMetaObject *ROSInterfaceBase::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ROSInterfaceBase::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ROSInterfaceBase.stringdata))
        return static_cast<void*>(const_cast< ROSInterfaceBase*>(this));
    return QObject::qt_metacast(_clname);
}

int ROSInterfaceBase::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
struct qt_meta_stringdata_ROSSubBase_t {
    QByteArrayData data[8];
    char stringdata[123];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    offsetof(qt_meta_stringdata_ROSSubBase_t, stringdata) + ofs \
        - idx * sizeof(QByteArrayData) \
    )
static const qt_meta_stringdata_ROSSubBase_t qt_meta_stringdata_ROSSubBase = {
    {
QT_MOC_LITERAL(0, 0, 10),
QT_MOC_LITERAL(1, 11, 20),
QT_MOC_LITERAL(2, 32, 0),
QT_MOC_LITERAL(3, 33, 18),
QT_MOC_LITERAL(4, 52, 17),
QT_MOC_LITERAL(5, 70, 16),
QT_MOC_LITERAL(6, 87, 15),
QT_MOC_LITERAL(7, 103, 18)
    },
    "ROSSubBase\0receiveMessageSignal\0\0"
    "startReceiveSignal\0stopReceiveSignal\0"
    "startReceiveSlot\0stopReceiveSlot\0"
    "receiveMessageSlot\0"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_ROSSubBase[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   44,    2, 0x06,
       3,    0,   45,    2, 0x06,
       4,    0,   46,    2, 0x06,

 // slots: name, argc, parameters, tag, flags
       5,    0,   47,    2, 0x0a,
       6,    0,   48,    2, 0x0a,
       7,    0,   49,    2, 0x09,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void ROSSubBase::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        ROSSubBase *_t = static_cast<ROSSubBase *>(_o);
        switch (_id) {
        case 0: _t->receiveMessageSignal(); break;
        case 1: _t->startReceiveSignal(); break;
        case 2: _t->stopReceiveSignal(); break;
        case 3: _t->startReceiveSlot(); break;
        case 4: _t->stopReceiveSlot(); break;
        case 5: _t->receiveMessageSlot(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (ROSSubBase::*_t)();
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&ROSSubBase::receiveMessageSignal)) {
                *result = 0;
            }
        }
        {
            typedef void (ROSSubBase::*_t)();
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&ROSSubBase::startReceiveSignal)) {
                *result = 1;
            }
        }
        {
            typedef void (ROSSubBase::*_t)();
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&ROSSubBase::stopReceiveSignal)) {
                *result = 2;
            }
        }
    }
    Q_UNUSED(_a);
}

const QMetaObject ROSSubBase::staticMetaObject = {
    { &ROSInterfaceBase::staticMetaObject, qt_meta_stringdata_ROSSubBase.data,
      qt_meta_data_ROSSubBase,  qt_static_metacall, 0, 0}
};


const QMetaObject *ROSSubBase::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ROSSubBase::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ROSSubBase.stringdata))
        return static_cast<void*>(const_cast< ROSSubBase*>(this));
    return ROSInterfaceBase::qt_metacast(_clname);
}

int ROSSubBase::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = ROSInterfaceBase::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}

// SIGNAL 0
void ROSSubBase::receiveMessageSignal()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void ROSSubBase::startReceiveSignal()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}

// SIGNAL 2
void ROSSubBase::stopReceiveSignal()
{
    QMetaObject::activate(this, &staticMetaObject, 2, 0);
}
QT_END_MOC_NAMESPACE
