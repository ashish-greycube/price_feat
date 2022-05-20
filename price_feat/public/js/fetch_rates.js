frappe.ui.form.on(cur_frm.doc.doctype, {
	refresh: function (frm) {
		var me = this;
		let promises = [];      
        let item_code_rates=[]  
        if (frm.doc.docstatus==0 && frm.is_new()==undefined) {
            frm.add_custom_button(__('Fetch Last Transaction Rate'), () => {
                frm.doc.items.forEach(function(d) {
                    let p = new Promise(resolve => {
                        if(d.item_code) {
                            frappe.call({
                                method: "price_feat.api.fetch_latest_customer_price",
                                args: {
                                    'doctype': frm.doc.doctype,
                                    'item_code':d.item_code
                                }
                            }).then((r) => {
                                if(r.message && r.message.length>0) {
                                    let rate=r.message[0].rate
                                    let item_hex_name=d.name
                                    item_code_rates.push({'name':item_hex_name,'rate':rate})
                                    resolve();
                                }else{
                                    resolve(); 
                                }
                            });
                        } 
                    });        
                    promises.push(p);
                }, this);
                Promise.all(promises).then(() => {
                    item_code_rates.forEach(element => {
                        let items=frm.doc.items
                        for (let index = 0; index < items.length; index++) {
                            const item = items[index];
                            if (item.name==element.name) {
                                item.rate=element.rate
                            }
                        }
                        frm.refresh_field('items')
                        frm.save()
                    });
                })
            })          
        }

    }
})